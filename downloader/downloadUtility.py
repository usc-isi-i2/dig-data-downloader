from file_downloader import FileDownloader
import sys
import traceback

import os, shutil

def run( dst_path, datasetconfig, clean_dst=False, force_download=True,
        run_on=None, overwrite_current_date=None, run_seed_data=False, use_downloaded=False):

    try:
        #dataset=datasetconfig["where_to_download"]["identifier"]
        print('\n> processing', datasetconfig["where_to_download"]["identifier"])

        #src_dataset_path = os.path.join(src_path, dataset)
        dst_dataset_path = os.path.join(dst_path, datasetconfig["where_to_download"]["identifier"]) # i
        # print src_dataset_path, dst_dataset_path

        if os.path.exists(dst_dataset_path) and clean_dst:
            shutil.rmtree(dst_dataset_path)

        # download
        if not run_seed_data and not use_downloaded:
            if run_on is None or 'download' in run_on:
                print('File Downloads:')
                fs = FileDownloader( dst_dataset_path)
                fs.process(datasetconfig,force=force_download, current_datetime=overwrite_current_date)


    except Exception as e:
        print('exception in run',e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print(''.join(lines))

if __name__ == '__main__':
    datasetconfig = {
        "where_to_download": {
        "frequency": "quarterly",
        "method": "get",
        "file_type": "csv",
        "template": "https://api.tradingeconomics.com/historical/country/all/indicator/Inflation%20Rate/{date_start}/{date_end}?c=h5gsaw1lfiaezah:hmee4m9qqhrbh62&format=csv",
        "replication": {
            "date_start":{
                "format": "%Y-%m-%d",
                "delta": -92
            },
            "date_end":{
                "format": "%Y-%m-%d"
            }
        },
        "identifier": "inflation_rate"
        },
        "how_to_process": "Event"
    }
    run("download/",datasetconfig)