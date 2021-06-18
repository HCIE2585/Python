代码情况说明：
    
    lab1 
        使用netmiko登陆一个H3C防火墙示例，并且将设备当前配置保存到本地
    lab2 
        使用netmiko登陆一个H3C交换机示例，并且将设备当前配置保存到本地
        主要介绍netmiko对设备的配置
            send_command()
            send_config_set()
            send_config_from_file()
    lab3
        展示textfsm模块的使用，配合ntc模块，可以将输入内容转换为json格式，对json格式内容进加工，得到想要的数据