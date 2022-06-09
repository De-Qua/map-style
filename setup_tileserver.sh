curdir=$(pwd)
cd tileserver_files/fonts/fonts
npm install
node ./generate.js
cd $curdir
mv tileserver_files/fonts/fonts/_output/* tileserver_files/fonts
rm -rf tileserver_files/fonts/fonts
