# !/bin/bash

# install python deps
uv sync
# install client deps
npm install --prefix client
# build client
npm run build --prefix client
