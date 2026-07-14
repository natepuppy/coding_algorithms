# Implement a key-value store that can serialize multiple string key-value 
# pairs into a single string and deserialize it back. Both keys and values 
# can contain any characters including delimiters, newlines, and special 
# characters. For example, serializing {"key:1": "val=ue", "k\ney": "v"} 
# should produce a string that can be deserialized back to the exact same 
# dictionary.

def serialize(object):
    string = ""
    for key, value in object.items():
        key_length = len(key)
        value_length = len(value)

        string += str(key_length) + "#" + key
        string += str(value_length) + "#" + value
    
    return string

def deserialize(string):
    result = {}

    length = 0
    i = 0
    key = None

    while i < len(string):
        char = string[i]

        if char == "#":
            i += 1
            new_val = []
            for j in range(i, i + length): # 2, 6
                new_val.append(string[j])
            
            if key == None:
                key = "".join(new_val)
                result[key] = None
            else:
                result[key] = "".join(new_val)
                key = None
            
            i += length
            length = 0
        else:
            val = int(char)
            length *= 10
            length += val
            i += 1
    
    return result

# python open_ai/kv_encoding.py
if __name__ == "__main__":
    obj = {"key:1": "val=ue", "k\ney": "v"}

    serialized_string = serialize(obj)
    result = deserialize(serialized_string)

    print(result)

    assert result == obj
    
    print("All tests passed")


