#!/bin/bash
command=""
statement="while true; do CMDS; done"
screen -S "Program" bash -c "${statement/CMDS/$command}"