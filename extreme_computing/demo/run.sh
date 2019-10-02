OUTPUT_DIR=/user/${USER}/assignment/demo
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=${USER}_demo_genres \
    -input /data/large/imdb/title.basics.tsv \
    -output $OUTPUT_DIR \
    -mapper mapper.py \
    -combiner reducer.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py

hdfs dfs -cat ${OUTPUT_DIR}/part-* | sort > $OUTPUT_FILE
cat $OUTPUT_FILE
