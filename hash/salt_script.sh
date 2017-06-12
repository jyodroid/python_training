Salt=Seg20162
password=239257

echo MD5
ts=$(date +%N)
echo -n $password$Salt | md5sum
tt=$(($(date +%N) - $ts))
echo "Tiempo MD5: $tt nanosegundos"

echo -------------------------------------

echo SHA256
ts=$(date +%N)
echo -n $password$Salt | sha256sum
tt=$(($(date +%N) - $ts))
echo "Tiempo SHA256: $tt nanosegundos"

echo -----------------------------------

echo SHA512
ts=$(date +%N)
echo -n $password$Salt | sha512sum
tt=$(($(date +%N) - $ts))
echo "Tiempo SHA512: $tt nanosegundos"
l
