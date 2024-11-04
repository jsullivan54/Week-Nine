#“Write a program that asks the user to enter a distance in kilometers, /
# then converts that distance to miles. The conversion formula is as follows:
        #Miles = Kilometers × 0.6214”

print('Hello Master Wayne_Jung')

def main():
    km = int(input('Please Enter the Distance in Kilometers: '))
    answer= convert(km)
    print(f'The miles traveled is {answer:.1f}')


def convert (Kilomiter):
    miles= Kilomiter*0.6214
    return miles
    print(f'The miles traveled is:  {answer:.1f} miles')
main()



