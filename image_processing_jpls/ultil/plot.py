from matplotlib import pyplot as plt
def plot_image(image):
    plt.figure(figsize=(17,4))
    plt.imshow(image)
    plt.axis('off')
    plt.show()
def plot_result(*args):
    figm, ax = plt.subplots(1,len(args), figsize=(12,4))
    names_list=[f'image{i}' for i in range(1,len(args))]
    names_list.append('Resultado')
    for ax, image, name in zip(ax, args, names_list):
        ax.set_title(name)
        ax.imshow(image,cmap='gray')    
        ax.axis('off')
    figm.tight_layout()
    plt.show()
def plot_histogram(image):
    figm,ax=plt.subplots(1,3,figsize=(12,4),sharey=True,sharex=True)
    colors=['red','green','blue']
    for index,(ax,color) in enumerate(zip(ax,colors)): 
        ax.set_title(f'{color.title} Histograma')
        ax.hist(image[:,:,index].ravel(), bins=256, color=color,alpha=0.5)
    figm.tight_layout()
    plt.show()
       