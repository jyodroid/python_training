Salt=Seg20162
password=239257

echo MD5
ts=$(gdate +%N)
echo -n $password$Salt | (md5sum || md5)
tt=$(($(gdate +%N) - $ts))
echo "Tiempo MD5: $tt nanosegundos"

echo -------------------------------------

echo SHA256
ts=$(gdate +%N)
echo -n $password$Salt | (sha256sum || shasum -a 256)
tt=$(($(gdate +%N) - $ts))
echo "Tiempo SHA256: $tt nanosegundos"

echo -----------------------------------

echo SHA512
ts=$(gdate +%N)
echo -n $password$Salt | (sha512sum || shasum -a 512)
tt=$(($(gdate +%N) - $ts))
echo "Tiempo SHA512: $tt nanosegundos"
