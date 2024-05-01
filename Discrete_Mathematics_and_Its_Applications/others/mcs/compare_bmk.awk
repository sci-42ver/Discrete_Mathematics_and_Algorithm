#! /bin/awk -f
# Use `pdf-bookmark -p ~/Discrete_Mathematics_and_Algorithm/Discrete_Mathematics_and_Its_Applications/others/mcs/mcs.pdf > mcs.bmk` to generate bmk
# Then `summary=0;id2c "./compare_bmk.awk -v summary=$summary mcs.bmk" "./compare_bmk.awk -v summary=$summary mcs_2018.bmk" | less_n`
BEGIN {
  target_num=1
  # here maybe passed to bash which will transform \\ to \ https://stackoverflow.com/a/25867768/21294350
  target_subchapter_num=target_num"\\.[0-9]+"
  chapter_start=0
  start=0
  end=0
  len=0
  summary=summary
}
{
  # https://stackoverflow.com/a/21479520/21294350
  chapter_regex_pattern="^ +"target_num" .*\\.+([0-9]+)$"
  subchapter_start_regex_pattern="^ +"target_num"\\.1 .*\\.+([0-9]+)$"
  subchapter_regex_pattern="^ +"target_num"\\.([2-9]) .*\\.+([0-9]+)$"
  subchapter_regex_pattern_2="^ +"target_num"\\.([0-9][0-9]+) .*\\.+([0-9]+)$"
  first_problem_pattern="^ +Problem "target_num"\\.1\\.+([0-9]+)$"
  # https://stackoverflow.com/a/4673336/21294350
  if (match($0, chapter_regex_pattern, a)) {
    # print $0 ";" a[1]
    chapter_start=a[1]
  }
  if (match($0, subchapter_start_regex_pattern, a)) {
    # print $0 ";" a[1]
    start=a[1]
    last_subchapter=1
  }
  # Notice the order where 1x is checked first to avoid unnecessary useless match()
  if (match($0, subchapter_regex_pattern_2, a) || match($0, subchapter_regex_pattern, a)) {
    # print $0 ";" a[2]
    end=a[2]
    len=int(end)-int(start)
    if (!summary) {
      # https://stackoverflow.com/a/46885991/21294350
      print target_num "." last_subchapter ":" len
    }
    start=a[2]
    last_subchapter=int(a[1])
  }
  if (match($0, first_problem_pattern, a)) {
    # print $0 ";" a[1]
    end=a[1]
    # https://stackoverflow.com/a/5810490/21294350
    if (summary) {
      len=int(end)-int(chapter_start)
      print target_num ":" len
    } else{
      len=int(end)-int(start)
      print "last chapter-" target_num "." last_subchapter ":" len
    }
    target_num=target_num+1
  }
}