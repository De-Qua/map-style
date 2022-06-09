curdir=$(pwd)
cd tileserver_files/fonts
git clone https://github.com/openmaptiles/fonts
mv inter fonts
cd fonts
npm install
node ./generate.js
cd $curdir
mv tileserver_files/fonts/fonts/_output/* tileserver_files/fonts
rm -rf tileserver_files/fonts/fonts
