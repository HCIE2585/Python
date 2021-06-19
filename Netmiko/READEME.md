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
    lab4
        通过netmiko登陆多台设备进行配置和信息查询，设备除ip地址外，其他登陆参数保持不变
    lab5
        通过netmiko登陆多台设备，使用json数据格式，存储需要登陆的设备信息