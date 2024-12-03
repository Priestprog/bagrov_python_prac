r = "push sfd sdfsdf sdfsdf sdf"
match r.split():
    case ["mov", r1, r2]:
        print(f"moving {r2} to {r1} ")
    case ["push" | "pop" as cmd, *tail] if len(tail)>0:
        print(f"{cmd}ing", *tail)
    case [a,b]:
        print(f"making {a} with {b}")
    case _:
        print("parse erorr")