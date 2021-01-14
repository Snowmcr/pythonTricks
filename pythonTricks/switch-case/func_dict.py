func_dict = [
    "cond_a": handle_a:
    "cond_b": handle_b:
]
func_dict[cond]()
# It is like a switch, checking the cond's and doing the comparison

func_dict.get(cond, handle_default)()
# Better, in case of not having the condition we want, 
# it uses hanlde_default.