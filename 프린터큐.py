test=int(input())
for i in range(test):
    n,m=map(int, input().split())
    arr=list(map(int, input().split()))
    
    target=arr[m]
    queue=sorted(arr)
    queue.reverse()
    target+=0.5
    arr[m]+=0.5
    cnt=1
    while True:
        if int(arr[0])==queue[0]:
            if arr[0]==target:
                print(cnt)
                break
            arr.pop(0)
            queue.pop(0)
            cnt+=1
        else:
            arr.append(arr.pop(0))

            ada_param_grid = {'base_estimator__max_depth':[1,50],
          'base_estimator':[DecisionTreeClassifier(max_features=2), 
                            DecisionTreeClassifier(max_features=10)]}

ada_grid = GridSearchCV(estimator = AdaBoostClassifier(), param_grid= ada_param_grid, scoring=ftwo_scorer, verbose=1, n_jobs=-1, cv=5,)
ada_grid.fit(X_trainVal, y_trainVal)
print('Gridsearch by using f2 score')
print('best parameter : {}'.format(ada_grid.best_params_))
print('best f2 score of CV : {:.3f}'.format(ada_grid.best_score_))
print('best f2 score of test set:{:.3f}'.format(ada_grid.score(X_test, y_test)))
print("최고 성능 모델:\n", ada_grid.best_estimator_)