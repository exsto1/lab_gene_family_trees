library(ape)
library(phangorn)
library('TreeDist')

# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install(c("Biostrings", "seqLogo"))

# tree1 = read.tree(file = "org_list_new_r.nwk")
# tree2 = read.tree(file = "seqdump_phy_phyml/ml_tree.nwk")
# 
# distance <- RF.dist(tree1, tree2, normalize = FALSE, rooted = FALSE)
# print(distance)
# VisualizeMatching(ClusteringInfoDistance, tree1, tree2)


tree1 = read.tree(file = "test/test11.nwk")
tree2 = read.tree(file = "test/test22.nwk")

distance <- RF.dist(tree1, tree2, normalize = FALSE, rooted = FALSE)
print(distance)
VisualizeMatching(ClusteringInfoDistance, tree1, tree2)
