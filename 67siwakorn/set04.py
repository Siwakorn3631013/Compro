attendance_week = [
    ["alice", "Bob" , "charlie" , "David"],
    ["alice", "charlie", "david"],
    ["alice", "Bob","David"],
    ["alice", "charlie", "David"]
]


attence_sets = [set(day) for day in attendance_week]
print(attence_sets)

