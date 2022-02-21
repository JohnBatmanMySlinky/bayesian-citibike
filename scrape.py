import requests
import json
from datetime import datetime, date, timedelta
import time
import os
from args import parse_args_main

def get_data(url):
    dat = requests.get(url).json()
    return dat['last_updated'], dat['data']

def get_end_time(RUN_LENGTH):
    return datetime.now() + timedelta(seconds = RUN_LENGTH)

def dump(session_data, SAVE_DIR, end_time):
    today = date.today()
    dump_dir = os.path.join(SAVE_DIR, str(today))
    dump_file = os.path.join(dump_dir, str(end_time))

    if not os.path.exists(dump_dir):
        os.mkdir(dump_dir)

    with open(dump_file + '.txt', 'w') as outfile:
        json.dump(session_data, outfile)

    return True

def run(URL, SLEEP_SECONDS, RUN_LENGTH, SAVE_DIR, verbose=False):
    # set up
    end_time = get_end_time(RUN_LENGTH)
    now = datetime.now()
    session_data = {}

    # start collecting
    while now <= end_time:
        # get data
        k, v = get_data(URL)
        session_data[k] = v
        if verbose: print(f"data collected for {k}")

        # rest
        time.sleep(SLEEP_SECONDS)
        now = datetime.now()

    # save data to disk
    dump(session_data, SAVE_DIR, end_time)

    return True

if __name__ == "__main__":
    URL = "https://gbfs.citibikenyc.com/gbfs/es/station_status.json"
    SAVE_DIR = '/extradata/citibikedata'

    args = parse_args_main()
    RUN_LENGTH = args.run_for
    SLEEP_SECONDS = args.sleep_for
    verbose = args.verbose == 'true'

    run(
        URL=URL,
        SLEEP_SECONDS=SLEEP_SECONDS,
        RUN_LENGTH=args.run_for,
        SAVE_DIR=SAVE_DIR,
        verbose=verbose
    )
