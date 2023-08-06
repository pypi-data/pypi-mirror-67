#!/usr/bin/env bash

rm -f /tmp/copy.sqlk
cp ~/.ch2/database.sqlk /tmp/copy.sqlk

sqlite3 /tmp/copy.sqlk <<EOF
pragma foreign_keys = on;
delete from source where type != 3;
delete from statistic_name where id in (
  select statistic_name.id from statistic_name
    left outer join statistic_journal
      on statistic_journal.statistic_name_id = statistic_name.id
   where statistic_journal.id is null
);
EOF

rm -f /tmp/dump-k.sql
sqlite3 /tmp/copy.sqlk <<EOF
.output /tmp/dump-k.sql
.mode insert source
select * from source;
.mode insert statistic_journal
select * from statistic_journal;
.mode insert statistic_journal_float
select * from statistic_journal_float;
.mode insert statistic_journal_integer
select * from statistic_journal_integer;
.mode insert statistic_journal_text
select * from statistic_journal_text;
.mode insert statistic_name
select * from statistic_name;
.mode insert topic
select * from topic;
.mode insert topic_field
select * from topic_field;
.mode insert topic_journal
select * from topic_journal;
EOF

rm -f ~/.ch2/database.sqll
dev/ch2 no-op

sqlite3 ~/.ch2/database.sqll < /tmp/dump-k.sql

dev/ch2 default-config --no-diary
dev/ch2 constants --set FTHR.Bike 154
