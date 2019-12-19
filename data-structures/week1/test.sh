for i in `seq -w 1 22`; do
  input=$(cat tests/"$i")
  my_output=$(echo "$input" | python3 network_simulation.py)
  expected_output=$(cat tests/"$i".a)
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
