import re

def compute_incremented_first_part(s, nb_start_index, nb_end_index):
    extracted_nb_str = s[nb_start_index:nb_end_index] if nb_start_index < len(s) else "0"
    nb = int(extracted_nb_str) + 1

    ending_index_first_part = nb_start_index
    
    if extracted_nb_str == "0":
        extracted_nb_str = ""

    if len(str(nb)) == len(extracted_nb_str) + 1 and s[nb_start_index-1:nb_start_index] == "0":
        ending_index_first_part = nb_start_index - 1

    first_part = s[0:ending_index_first_part]

    return f"{first_part}{nb}"

def increment_string(s):
    result_regexes = [m for m in re.finditer(r"[1-9]+",s)]
    result_regex = result_regexes[-1] if len(result_regexes) > 0 else None

    if not result_regex or (len(s) and s[-1] == "0"):
        return compute_incremented_first_part(s, len(s), -1)

    nb_start_index = result_regex.start()
    nb_end_index = result_regex.end()

    recomputed_first_part = compute_incremented_first_part(s, nb_start_index, nb_end_index)
    recomputed_last_part = s[nb_end_index:len(s)]

    new_result = f"{recomputed_first_part}{recomputed_last_part}"

    return new_result

assert increment_string("foo") == "foo1"
assert increment_string("fooi012ia") == "fooi013ia"
assert increment_string("foobar23") == "foobar24"
assert increment_string("foobar0042") == "foobar0043"
assert increment_string("foo9") == "foo10"
assert increment_string("foo099") == "foo100"
assert increment_string("foo0099ii") == "foo0100ii"
assert increment_string("foobar00") == "foobar01"

assert increment_string("<3700000000339") == "<3700000000340"
assert increment_string("EJSV#5u%t714H_78xC8Du@3852722108?3197985ZaZR854377$Vsp,tw998933Wm2iU{FCX4?3Sy?2KYHP50269410000000") == "EJSV#5u%t714H_78xC8Du@3852722108?3197985ZaZR854377$Vsp,tw998933Wm2iU{FCX4?3Sy?2KYHP50269410000001"


