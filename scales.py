def get_scale_midi():
    notes=[]
    count=0
    for i in range(0,50):
        if count< 109:
            notes.append(count)
            count += 2
    print(notes)            
    
class Scale:
    keys = {"a":-3,
            "a#":-2,
            "b":-1,
            "c":0,
            "c#":1,
            "d":2,
            "d#":3,
            "e":4,
            "f":5,
            "f#":6,
            "g":7,
            "g#":8,
            }

    scales =   {"fifths":
                        {"notes":[0, 7, 14, 21,
                                28, 35, 42, 49,
                                56, 63, 70, 77,
                                84, 91, 98, 105],
                        "divisor": 4},

                "pentatonic":
                        {"notes":[0, 3, 5, 7, 10, 12, 15, 17, 19, 22, 24,
                                27, 29, 31, 34, 36, 39, 41, 43, 46, 48,
                                51, 53, 55, 58, 60, 63, 65, 67, 70, 72,
                                75, 77, 79, 82, 84,87, 89, 91, 94, 96,
                                9, 101, 103, 106, 108,111, 113, 115, 118],
                        "divisor": 10},

                "whole_tones":
                        {"notes":[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,
                                26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48,
                                50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72,
                                74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98],
                        "divisor":10}    

    }
    def process(val,key,scl):    

        note = 100- val/Scale.scales[scl]["divisor"]
        value = min(Scale.scales[scl]["notes"],key=lambda x:abs(x - note)) + Scale.keys[key]
        return value
        

#Scale.process(130,"g#","pentatonic")