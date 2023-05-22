import json
from mpi4py import MPI

mpi_comm = MPI.COMM_WORLD
mpi_rank = mpi_comm.Get_rank()
mpi_size = mpi_comm.Get_size()

with open("twitter-huge.json", 'r', encoding='UTF-8') as f:
    count = 0
    num = 0
    tweet_line = ''
    
    while True:
        line = f.readline()
        count += 1

        if line == '':
            break

        if count % mpi_size == mpi_rank:
            if line.find("tourism") != -1 or line.find("travel") != -1 or line.find("travelling") != -1:
                new_result = {}
                line = line.strip().rstrip(',')
                json_line = json.loads(line)
                if "value" in json_line.keys():
                    new_result["value"] = json_line["value"]
                if "lang" in json_line["doc"]["data"].keys():
                    new_result["lang"] = json_line["doc"]["data"]["lang"]
                if "text" in json_line["doc"]["data"].keys():
                    new_result["text"] = json_line["doc"]["data"]["text"]
                if "sentiment" in json_line["doc"]["data"].keys():
                    new_result["sentiment"] = json_line["doc"]["data"]["sentiment"]
                if "includes" in json_line["doc"].keys():
                    new_result["includes"] = json_line["doc"]["includes"]

                tweet_line += json.dumps(new_result)
                tweet_line += '\n'
                num += 1


data = mpi_comm.gather(tweet_line, root=0)
num = mpi_comm.gather(num, root=0)

all = ''
all_num = 0
if mpi_rank == 0:
    for i in range(0, mpi_size):
        all += data[i]
        all_num += num[i]
    with open("twitter_output.json", "w") as file:
        file.write(all)
    print(all_num)

