a=`sudo docker run -d -P upython` 
b=`sudo docker port $a | tail -c 6`

c=`cat details.txt`
echo  "$c -p $b" 

