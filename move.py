from box import action


if __name__ != '__main__':
    def get_actions():
        actions = []
        ##############  WRITE YOUR CODE HERE    #############
    
    
        for i in range(18):
            if 0 <= i <= 2:
                actions.append(action.move_right)
            elif 3 <= i < 5:
                actions.append(action.move_down)
    
    
    
    
        #####################################################
    
        return actions

if __name__ == '__main__':
    pass