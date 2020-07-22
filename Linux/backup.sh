#!/bin/bash
cd "$(dirname "$0")" # This makes it semi-portable
tar -zcvf backup/$(date +%s).tar world