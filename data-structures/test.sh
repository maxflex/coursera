dir="week3/$1/tests/"
app="week3/$1/$1.py"
for i in `seq -w $2 $2`; do
  input=$(cat "$dir$i")
  my_output=$(echo "$input" | python3 "$app")
  expected_output=$(cat "$dir$i".a)
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