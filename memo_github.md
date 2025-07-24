### docs 폴더만 클론

git clone --filter=blob:none --no-checkout https://github.com/Rookie-YangHM/codyssey.git<br>
cd codyssey<br>
git sparse-checkout init --cone<br>
git sparse-checkout set docs<br>
git checkout`