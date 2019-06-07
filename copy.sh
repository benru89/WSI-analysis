for f in dataset_patches_level0/positive_patches/*; do
  echo $f
  j=0
  for i in $f/*; do 
    echo $i
    cp "$i" level0/$f$j; 
    j=`expr $j + 1`
    done
done
