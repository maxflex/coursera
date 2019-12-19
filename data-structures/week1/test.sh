for i in `seq -w 1 $2`; do
  input=$(cat "$1"/tests/"$i")
  my_output=$(echo "$input" | python3 "$1"/"$1".py)
  expected_output=$(cat "$1"/tests/"$i".a)
  if [ "$my_output" != "$expected_output" ]; then
    echo "==== TEST $i===="
    echo "Input: \n$input"
    echo "---------------"
    echo "My output: \n$my_output"
    echo "---------------"
    echo "Expected: \n$expected_output"
    exit 1
  fi
done
echo "Success"