from audioset_strong_download import Downloader
d = Downloader(root_path='test', labels=["Speech", "Afrobeat"], n_jobs=2, download_type='eval', dataset_ver='strong', copy_and_replicate=False)
d.download(format = 'vorbis')
