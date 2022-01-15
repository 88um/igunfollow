import os, time
try:
    import stdiomask
    from InstagramAPI import InstagramAPI
    from random import randint
except:
    os.system('pip install InstagramAPI')
    os.system('pip install random')
    os.system('pip install stdiomask')
    import stdiomask
    from InstagramAPI import InstagramAPI
    from random import randint


banner = ("""
               __      _ _                
              / _|    | | |               
  _   _ _ __ | |_ ___ | | | _____      __ 
 | | | | '_ \|  _/ _ \| | |/ _ \ \ /\ / / 
 | |_| | | | | || (_) | | | (_) \ V  V /  
  \__,_|_| |_|_| \___/|_|_|\___/ \_/\_/
  
        ~By Crackled on tele.~

                                        """)



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)


def login():
    global ig, nam
    while True:
        clear()
        nam = input('[+] Username: ')
        pas = stdiomask.getpass('[+] Password: ')
        ig = InstagramAPI(nam, pas)
        success = ig.login()
        if not success:
            time.sleep(6)
        else:
            break
    main()
    


def main():
    global  unf, speed
    while True:
                clear()
                print(f'[-] Logged in user: {nam}\n')
                unf = int(input('[+] How many people to unfollow: '))
                speed = input("""[-] Determine your Unfollow speed\n\n[1] Fast 10-15 sec delay
[2] Medium 20-30 sec delay
[3] Slow 45-90 sec delay\n\n[+] Choose One: """)
                if speed == '1':
                    speed = randint(10,15)
                    Unfollow()
                elif speed == '2':
                    speed = randint(20,30)
                    Unfollow()
                elif speed == '3':
                    speed = randint(45,90)
                    Unfollow()
                else:
                    pass


def GetAllFollowing(bot, user_id):
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = bot.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(bot.LastJson.get('users', []))
        next_max_id = bot.LastJson.get('next_max_id', '')
    following = set([_['pk'] for _ in following])
    return following




def Unfollow():
    done = 0
    error = 0
    err = 0
    ig.getSelfUsernameInfo()
    self_id = ig.LastJson['user']['pk']
    following = GetAllFollowing(ig, self_id)
    print('\n[+] Unfollowing {}/{} users'.format(unf, len(following)))
    time.sleep(9)
    for usr in list(following)[:min(len(following), unf)]:
        try:
            ig.getUsernameInfo(str(usr))
            user = ig.LastJson['user']['username']
            ig.unfollow(str(usr))
            done+=1
            clear()
            print(f"[-] Done: {done} | Errors: {err} | Last Unfollowed: {user}")
            time.sleep(speed)
        except KeyboardInterrupt:
            return
        except:
            err+=1
            error+=1
            print('\n[!] First Error in unfollowing (maybe soft block)...sleep 15 min')
            if error == 3:
                print('[!] 3x Error in unfollowing...sleep one hour')
                time.sleep(3601)
                error = 0
            else:
                time.sleep(901)
    
    print('\n[DONE] Unfollowed all users! Returning to main function. ')
    time.sleep(9)
    
        

if __name__ == "__main__":
    login()