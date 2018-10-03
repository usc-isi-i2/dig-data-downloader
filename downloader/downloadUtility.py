from file_downloader import FileDownloader
import sys
import traceback

import os
import shutil

def run( dst_path, datasetconfig, clean_dst=False, force_download=True, overwrite_current_date=None):

    try:
        print('\n> processing', datasetconfig["where_to_download"]["identifier"])
        dst_dataset_path = os.path.join(dst_path, datasetconfig["where_to_download"]["identifier"])

        if os.path.exists(dst_dataset_path) and clean_dst:
            shutil.rmtree(dst_dataset_path)

        # download
        print('File Downloads:')
        fs = FileDownloader( dst_dataset_path)
        fs.process(datasetconfig,force=force_download, current_datetime=overwrite_current_date)


    except Exception as e:
        print('exception in run',e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print(''.join(lines))

if __name__ == '__main__':
    datasetConfig = {
        "where_to_download": {
        "frequency": "quarterly",
        "method": "get",
        "file_type": "csv",
        "template": "https://api.tradingeconomics.com/historical/country/all/indicator/Inflation%20Rate?c=guest:guest&format=csv",
        "replication": {
        },
        "identifier": "inflation_rate"
        },
        "how_to_process": "Event"
    }
    run("download/",datasetConfig)