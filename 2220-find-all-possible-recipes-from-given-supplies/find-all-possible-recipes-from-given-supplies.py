class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recipes_d = {
            k: v for k, v in zip(recipes, ingredients)
        }

        order = []
        vis = set()
        def rec(recipe):
            vis.add(recipe)
            for r in recipes_d[recipe]:
                if r in recipes_d and r not in vis:
                    rec(r)
            order.append(recipe)
        
        for r in recipes:
            if r not in vis:
                rec(r)
        
        ans = []
        for r in order:
            if all([i in supplies for i in recipes_d[r]]):
                ans.append(r)
                supplies.add(r)

        return ans
