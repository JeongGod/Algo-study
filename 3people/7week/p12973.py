def solution(s):
  st = []
  for el in s:
    if st:
      if st[-1] == el:
        st.pop()
      else:
        st.append(el)
    else:
        st.append(el)
  return 0 if st else 1