osember = input(f'dobja egy osember nevet')
bogyo = int(input('hany bogyo {osember}-nak'))
if bogyo < 10 :
    minosites = 'zsenge'
elif bogyo < 20 :
    minosites = 'magy koponya'
else:
    minosites = 'gyujtiogetop'

print(f'{osember} egy {minosites}')
