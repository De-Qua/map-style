outputdir=_tileserver_folder
curdir=$(pwd)
cp -r tileserver_files $outputdir
cd $outputdir/fonts
git clone https://github.com/openmaptiles/fonts
mv inter fonts
cd fonts
npm install
node ./generate.js
cd $curdir
mv $outputdir/fonts/fonts/_output/* $outputdir/fonts
rm -rf $outputdir/fonts/fonts
rm -rf $outputdir/package-lock.json
