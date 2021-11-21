library(ape)
library(phangorn)
library(ggplot2)
library(reshape2)
library("TreeDist")

# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install(c("Biostrings", "seqLogo"))


tree1 = read.tree(file = "../trees/ml_tree.txt")
tree2 = read.tree(file = "../trees/mp_tree.treefile")
tree3 = read.tree(file = "../trees/nj_tree.tre")
trees = c(tree1, tree2, tree3)


distance1 <- RF.dist(tree1, tree2, normalize = FALSE, rooted = FALSE)
distance2 <- RF.dist(tree1, tree3, normalize = FALSE, rooted = FALSE)
distance3 <- RF.dist(tree2, tree3, normalize = FALSE, rooted = FALSE)

VisualizeMatching(ClusteringInfoDistance, tree1, tree2)

# results = matrix(nrow = 3, ncol = 3)
# for (treex in 1:3){
#   for (treey in 1:3){
#     distance = RF.dist(trees[[treex]], trees[[treey]], normalize = FALSE, rooted = FALSE)
#     print(distance)
#     results[treex, treey] = distance
#   }
# }
# 
# longData<-melt(results)
# ggplot(longData, aes(x = Var2, y = Var1)) + 
#   geom_raster(aes(fill=value)) + 
#   geom_text(aes(label = round(value, 1)))
# # print(distance)
# 
