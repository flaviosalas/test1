import subprocess

def run_job(cmd):
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return ret.stdout.decode(('UTF-8'))
    
if __name__ == '__main__':
    # Compile
    run_job("gcc main.c")

    # Run
    msg = run_job("./a.out").rstrip()
    if msg == "Hola mundo!":
        print("Ok!")
    else:
        print("Error. The correct answer is `Hola mundo!`, but your outupt is:")
        print("```")
        print(msg)
        print("```")
