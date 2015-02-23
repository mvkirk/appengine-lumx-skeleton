#!/bin/sh
dev_appserver.py --datastore_path="./datastore" --blobstore_path="./blobstore" --search_indexes_path="./.search_index" --port 8888 ./app
