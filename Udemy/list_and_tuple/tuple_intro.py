"""t='a','b','c'
print(type(t))"""

albums=[('Welcome to my Nightmare','Alice Cooper',1975),
        ('Bad Company','Bad Company',1974),
        ('Nightflight','Budgie',1981),
        ('More Mayhem','Emilda May',2011),
        ('Ride the Lighting','Metallica',1984),
        ]

"""for album in albums:
    name,artist,year=album
    print('Album: {}, Artist: {}, Year: {}'.format(name,artist,year))"""

for (name,artist,year) in albums:
    print('Album: {}, Artist: {}, Year: {}'.format(name,artist,year))














"""title,artist,year=metallica
print(title)
print(artist)
print(year)


table=('Coffee tabke',200,100,75,34.50)
print(table[1]*table[2])

name,length,width,height,price=table
print(length*width)"""















"""print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2=list(metallica)
print(metallica2)
metallica2[0]='Master of puppets'
print(metallica2)"""