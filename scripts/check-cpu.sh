#!/bin/bash

os=$(uname -s)

if [[ "$os" == "Linux" ]]; then
  echo "Operating System: Linux"
elif [[ "$os" == "Darwin" ]]; then
  echo "Operating System: macOS"
  cpu=$(sysctl -n machdep.cpu.brand_string)
  echo "CPU: $cpu"
elif [[ "$os" == "FreeBSD" ]]; then
  echo "Operating System: FreeBSD"
elif [[ "$os" == "Windows" ]]; then
  echo "Operating System: Windows"
else
  echo "Unknown Operating System"
fi




