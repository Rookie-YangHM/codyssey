### docs 폴더만 클론

git clone --filter=blob:none --no-checkout https://github.com/Rookie-YangHM/codyssey.git
cd codyssey
git sparse-checkout init --cone
git sparse-checkout set docs
git checkout