import genshin
import star_rail
import config
import cookies

domain_name = '.hoyolab.com'
genshin_act_id = 'e202102251931481'
star_rail_act_id= 'e202303301540311'
_config = config.read_config()


if __name__ == "__main__":
    token = cookies.GetToken(browser=_config['browser'], domain_name=domain_name)
    genshin.Claim(act_id=genshin_act_id, cookie=token)
    star_rail.Claim(act_id=star_rail_act_id, cookie=token)
    