# -*- coding: utf-8 -*-

from datetime import datetime

from .request_api import RequestAPI


class SonarrAPI(RequestAPI):

    def __init__(
            self, 
            host_url: str, 
            api_key: str,
        ):
        """Constructor requires Host-URL and API-KEY

            Args:
                host_url (str): Host url to sonarr.
                api_key: API key from Sonarr. You can find this
        """
        super().__init__(host_url, api_key)

    #TODO: TEST
    def getCalendar(self, *args):
        """getCalendar retrieves info about when series were/will be downloaded.
           If start and end are not provided, retrieves series airing today and tomorrow.

            args:
                start_date:
                end_date: 
        
            Returns:
                json response

        """
        path = '/api/calendar'
        data = {}
        
        if len(args) == 2:
            start_date = args[0]
            end_date = args[1]
             
            if isinstance(start_date, datetime):
                startDate = start_date.strftime('%Y-%m-%d')
                data.update({
                    'start': startDate                
                })

            if isinstance(end_date, datetime):
                endDate = end_date.strftime('%Y-%m-%d') 
                data.update({
                    'end': endDate
                })

        res = self.request_get(path, **data)
        return res.json()

    def getCommand(self, *args):
        """getCommand Queries the status of a previously 
            started command, or all currently started commands.

            Args:
                Optional - id (int) Unique ID of command
            Returns:
                json response

        """
        if len(args) == 1:
            path = f'/api/command/{args[0]}'
        else:
            path = '/api/command'

        res = self.request_get(path)
        return res.json()

    def __setCommand(self, data):
        """Private Command Method
            
            Args:
                data (dict): data payload to send to /api/command

            Returns:
                json response
        """
        path = '/api/command'
        res = self.request_post(path, data)
        return res.json()  

    def RefreshSeries(self, *args):
        """RefreshSeries refreshes series information and rescans disk.

            Args:
                Optional - seriesId (int)        
            Returns:
                json response

        """
        data = {}
        if len(args) == 1: 
            data.update({
                'name': 'RefreshSeries',
                'seriesId': args[0]
            })
        else:
            data.update({
                'name': 'RefreshSeries'
            })
        return self.__setCommand(data)

    def RescanSeries(self, *args):
        """RescanSeries scans disk for any downloaded episodes for all or specified series.

            Args:
                Optional - seriesId (int)        
            Returns:
                json response

        """
        data = {}
        if len(args) == 1: 
            data.update({
                'name': 'RescanSeries',
                'seriesId': args[0]
            })
        else:
            data.update({
                'name': 'RescanSeries'
            })
        return self.__setCommand(data)

    def getDiskSpace(self):
        """GetDiskSpace retrieves info about the disk space on the server.
            
            Args: 
                None
            Returns:
                json response

        """
        path = '/api/diskspace'
        res = self.request_get(path)
        return res.json()



















    # TODO: Test this
    def getEpisodes(self, **kwargs):
        """Returns all episodes for the given series
            Args:
                series_id (int):
        
            Returns:
                json response
        """
        for key, value in kwargs.items():
            if key == 'seriesId':
                data = {
                    key: value
                }
                path = '/api/episode'
            elif key == 'episodeId':
                data = {
                    key: value
                }
                path = f'/api/episode/{value}'
        res = self.request_get(path, **data)
        return res.json()

    # TODO: Test this
    def getEpisode_by_episode_id(self, episode_id):
        """Returns the episode with the matching id
            Args:
                episode_id (int): 
        
            Returns:
                requests.models.Response: Response object form requests.
        """
        path = '/api/episode/{}'.format(episode_id)
        res = self.request_get(path)
        return res.json()   

    # TODO: Test this
    def upd_episode(self, data):
        """Update the given episodes, currently only monitored is changed, all 
        other modifications are ignored. All parameters (you should perform a 
        GET/{id} and submit the full body with the changes, as other values may 
        be editable in the future.

            Args: 
                data (dict): data payload

            Returns:
                requests.models.Response: Response object form requests.
        """
        path = '/api/episode'
        res = self.request_put(path, data)
        return res.json()

    # TODO: Test this
    def get_episode_files_by_series_id(self, series_id):
        """Returns all episode files for the given series

            Args:
                series_id (int):
        
            Returns:
                requests.models.Response: Response object form requests.
        """
        data = {
            'seriesId': series_id
        }
        path = '/api/episodefile'
        res = self.request_get(path, **data)
        return res.json()

    # TODO: Test this
    def get_episode_file_by_episode_id(self, episode_id):
        """Returns the episode file with the matching id

            Kwargs:
                episode_id (int):

            Returns:
                requests.models.Response: Response object form requests.     
        """
        path = '/api/episodefile/{}'.format(episode_id)
        res = self.request_get(path)
        return res.json()

    # TODO: Test this
    def rem_episode_file_by_episode_id(self, episode_id):
        """Delete the given episode file
        
            Kwargs:
                episode_id (str):

            Returns:
                requests.models.Response: Response object form requests. 
        """
        path = '/api/episodefile/{}'.format(episode_id)
        res = self.request_del(path, data=None)
        return res.json()

    # TODO: Test this
    def get_logs(self, **kwargs):
        """Gets Sonarr Logs

            Kwargs;
                page (int): Page number. Default 1.
                page_size (int): How many records per page. Default 50.
                sort_key (str): What key to sort on. Default 'time'.
                sort_dir (str): What direction to sort asc or desc. Default 
                desc.
                filter_key (str): What key to filter on. Default None.
                filter_value (str): What to filter on (Warn, Info, Error, All).
                Default All.

            Returns:
                requests.models.Response: Response object form requests.        
        """
        data = {
            'page': kwargs.get('page', 1),
            'pageSize': kwargs.get('page_size', 50),
            'sortKey': kwargs.get('sort_key', 'time'),
            'sortDir': kwargs.get('sort_dir', 'desc'),
            'filterKey': kwargs.get('filter_key', None),
            'filterValue': kwargs.get('filter_value', None)
        }
        if 'All' in data['filterValue'] or 'all' in data['filterValue']:
            data['filterValue'] = None

        path = '/api/log'
        res = self.request_get(path, **data)
        return res.json()

    # TODO: Work in progress.
    def serach_selected(self):
        pass

    # TODO: Test this
    def search_all_missing(self):
        """Gets all missing episodes and task's the indexer/downloader.
        
            Returns:
                requests.models.Response: Response object form requests. 
        """
        data = {
            'name': 'missingEpisodeSearch'
        }
        return self.command(data)


    # TODO: Test this
    def get_queue(self):
        """Gets current downloading info
        
            Returns:
                requests.models.Response: Response object form requests.
        """
        path = '/api/queue'
        res = self.request_get(path)
        return res.json()

    def get_quality_profiles(self):
        """Gets all quality profiles"""
        path = '/api/profile'
        res = self.request_get(path)
        return res.json()

    # TODO: Test this
    def push_release(self, **kwargs):
        """Notifies Sonarr of a new release.
            title: release name
            downloadUrl: .torrent file URL
            protocol: usenet / torrent
            publishDate: ISO8601 date string

            Kwargs:
                title (str): 
                downloadUrl (str):
                protocol (str):
                publishDate (str):

            Returns:
                requests.models.Response: Response object form requests.
        """
        path = '/api/release/push'
        res = self.request_post(path, data=kwargs)
        return res.json()

    def get_root_folder(self):
        """Returns the Root Folder"""
        res = self.request_get('/api/rootfolder')
        return res.json()

    # TODO: Test this
    def get_series(self):
        """Return all series in your collection
        
            Returns:
                requests.models.Response: Response object form requests.
        """
        path = '/api/series'
        res = self.request_get(path)
        return res.json()

    # TODO: Test this
    def get_series_by_series_id(self, series_id):
        """Return the series with the matching ID or 404 if no matching series 
        is found
        
            Args:
                series_id (int):

            Returns:
                requests.models.Response: Response object form requests.
        """
        path = '/api/series/{}'.format(series_id)
        res = self.request_get(path)
        return res.json()

    def construct_series_json(self, tvdbId, quality_profile):
        """Searches for new shows on trakt and returns Series object to add"""
        
        res = self.lookup_series(tvdbId)
        s_dict = res[0]

        # get root folder path
        root = self.get_root_folder()[0]['path']
        series_json = {
            'title': s_dict['title'],
            'seasons': s_dict['seasons'],
            'path': root + s_dict['title'],
            'qualityProfileId': quality_profile,
            'seasonFolder': True,
            'monitored': True,
            'tvdbId': tvdbId,
            'images': s_dict['images'],
            'titleSlug': s_dict['titleSlug'],
            "addOptions": {
                          "ignoreEpisodesWithFiles": True,
                          "ignoreEpisodesWithoutFiles": True
                        }
                    }
        return series_json

    def add_series(self, series_json):
        """Add a new series to your collection"""
        path = '/api/series'
        res = self.request_post(path, data=series_json)
        return res.json()

    # TODO: Test this
    def upd_series(self, data):
        """Update an existing series"""
        path = '/api/series'
        res = self.request_put(path, data)
        return res.json()

    # TODO: Test this
    def rem_series(self, series_id, rem_files=False):
        """Delete the series with the given ID"""
        # File deletion does not work
        data = {
            # 'id': series_id,
            'deleteFiles': 'true'
        }
        path = '/api/series/{}'.format(series_id)
        res = self.request_del(path, term)
        return res.json()

    def lookup_series(self, term):
        """Searches for new shows on tvdb"""
        if term.isdigit():
            term = f'tvdb:{term}'

        res = self.request_get(f'/api/series/lookup?term={term}')
        return res.json()

    def get_backups(self):
        """Returns the backups as json"""
        res = self.request_get('/api/system/backup')
        return res.json()

    def get_system_status(self):
        """Returns the System Status as json"""
        res = self.request_get('/api/system/status')
        return res.json()
