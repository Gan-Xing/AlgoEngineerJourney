# 培训班课程机器学习数学基础
# 线性代数 - 2h 啥也没记住（2024直播）
# 知乎搜索相关资料 -1h 路线了解
# 机器学习概述（2023录播）
# Scikit-learn 机器学习框架
# PyTorch 深度学习框架

# 公开数据集资源
# • http://archive.ics.uci.edu/ml/datasets.php
# • https://aws.amazon.com/cn/public-datasets/
# • https://www.kaggle.com/competitions
# • http://www.kdnuggets.com/datasets/index.html
# • http://www.sogou.com/labs/resource/list_pingce.php 
# • https://tianchi.aliyun.com/datalab/index.html
# • http://www.pkbigdata.com/common/cmptIndex.html
# • https://datafountain.cn/

# 模型的训练及测试


# AUC（Area Under the Curve）和ROC（Receiver Operating Characteristic）是与分类模型性能评估相关的概念，而召回率（Recall）、精确率（Precision）是与分类模型的预测结果相关的指标。让我分别解释它们之间的区别：

# 1. AUC（Area Under the Curve）和ROC（Receiver Operating Characteristic）：
#    - ROC是一个曲线，通常用于衡量二元分类模型的性能。它显示了在不同分类阈值下，真正例率（True Positive Rate，又称召回率）与假正例率（False Positive Rate）之间的关系。
#    - AUC是ROC曲线下的面积，表示分类模型在不同阈值下的性能总体情况。AUC的取值范围在0到1之间，AUC值越接近1，说明模型性能越好。

# 2. 召回率（Recall）和精确率（Precision）：
#    - 召回率（Recall）是指在所有真实正例中，模型成功预测为正例的比例。它关注模型找到所有正例的能力，公式为：Recall = TP / (TP + FN)，其中TP表示真正例，FN表示假负例。
#    - 精确率（Precision）是指在所有预测为正例的样本中，真正例的比例。它关注模型预测为正例的准确性，公式为：Precision = TP / (TP + FP)，其中TP表示真正例，FP表示假正例。

# 区别总结：
# - AUC和ROC主要用于评估分类模型整体性能，不关心具体的阈值设置。
# - 召回率和精确率则关注模型在特定阈值下的表现，用于更详细地了解模型的性能。
# - 召回率强调找到所有正例的能力，而精确率强调预测为正例的准确性。

# 在实际应用中，选择哪个指标取决于问题的需求和成本权衡。如果模型需要找到尽可能多的正例，可以重点关注召回率。如果模型需要确保正例预测的准确性，可以重点关注精确率。 AUC和ROC可以帮助您在不同问题场景下综合评估模型的性能。

# 模型训练
# 模型测试


# 机器学习开发通常包括多个阶段，以下是一般的机器学习开发流程，按顺序列出的步骤：

# 1. 定义问题：
#    - 确定问题的目标和范围。
#    - 收集并理解数据，明确问题的背景和需求。

# 2. 数据收集和准备：
#    - 收集与问题相关的数据，包括特征和标签。
#    - 清洗数据，处理缺失值、异常值和重复数据。
#    - 数据转换和标准化，将数据转换为可用于机器学习的格式。
#    - 划分数据集为训练集、验证集和测试集。

# 3. 特征工程：
#    - 选择合适的特征，可能需要进行特征选择或提取。
#    - 进行特征缩放、编码、归一化等预处理步骤。
#    - 创建新的特征，以提高模型性能。

# 4. 模型选择：
#    - 选择适当的机器学习算法，根据问题类型（分类、回归等）和数据。
#    - 建立模型的基线性能，以后续优化为比较依据。

# 5. 模型训练：
#    - 使用训练数据训练机器学习模型。
#    - 调整模型的超参数，以获得最佳性能。
#    - 监控训练过程，防止过拟合。

# 6. 模型评估：
#    - 使用验证集评估模型性能，包括准确率、召回率、精确率、F1值等指标。
#    - 可视化和分析模型的预测结果和错误。

# 7. 模型优化：
#    - 根据评估结果进行模型改进和优化。
#    - 可能需要尝试不同的特征工程方法、算法或模型架构。

# 8. 模型测试：
#    - 使用独立的测试集对最终模型进行评估，检查其在未见过的数据上的性能。

# 9. 模型部署：
#    - 将训练好的模型部署到生产环境中，以供实际使用。
#    - 集成模型到应用程序或系统中。

# 10. 模型监控和维护：
#     - 持续监控模型的性能，定期评估其在生产环境中的表现。
#     - 如果模型性能下降，可能需要重新训练或更新模型。

# 11. 文档和报告：
#     - 记录模型开发过程、数据处理方法、模型架构和性能指标。
#     - 撰写报告以便与团队成员和利益相关者分享结果。

# 12. 持续改进：
#     - 接受反馈，不断改进模型和流程。
#     - 参与持续学习和研究，以跟踪最新的机器学习技术和方法。

# 这些步骤构成了通用的机器学习开发流程，但具体的项目可能会根据问题的复杂性和需求而有所不同。成功的机器学习项目通常需要跨学科合作，包括数据科学家、机器学习工程师、领域专家和开发人员的协作。

# 首先判断是什么任务，分类任务还是回归任务
# 对任务进行分类为回归任务和分类任务是因为这两种任务类型在机器学习和统计建模中具有明显的差异，它们的目标和处理方式不同。任务分类有以下几种常见种类：

# 1. **回归任务（Regression Tasks）**：
#    - 目标：在回归任务中，目标是预测一个或多个连续数值型变量。例如，预测房价、股票价格、销售额等。
#    - 输出：回归模型的输出是一个实数或实数向量。
#    - 评估指标：通常使用均方误差（MSE）、均方根误差（RMSE）、平均绝对误差（MAE）等指标来衡量模型性能。

# 2. **分类任务（Classification Tasks）**：
#    - 目标：在分类任务中，目标是将输入样本分为不同的类别或标签。例如，垃圾邮件检测、图像分类、疾病诊断等。
#    - 输出：分类模型的输出是样本属于各个类别的概率或一个离散的类别标签。
#    - 评估指标：通常使用准确率（Accuracy）、召回率（Recall）、精确率（Precision）、F1值等指标来衡量模型性能。

# 3. **聚类任务（Clustering Tasks）**：
#    - 目标：在聚类任务中，目标是将数据集中的样本划分为多个簇，使得同一簇内的样本相似，而不同簇之间的样本不相似。
#    - 输出：聚类模型的输出是样本所属的簇或簇标签。
#    - 评估指标：聚类任务通常使用轮廓系数、互信息等指标来评估聚类的质量。

# 4. **降维任务（Dimensionality Reduction Tasks）**：
#    - 目标：降维任务旨在减少数据集的维度，同时保留关键信息。降维有助于可视化和减少计算复杂度。
#    - 方法：常见的降维方法包括主成分分析（PCA）、t-分布邻域嵌入（t-SNE）、线性判别分析（LDA）等。
#    - 评估指标：通常使用方差解释率等指标来评估降维的效果。

# 5. **生成任务（Generative Tasks）**：
#    - 目标：生成任务旨在生成新的数据，这些数据应该与原始数据集具有相似的分布。例如，生成对抗网络（GAN）用于图像生成。
#    - 方法：生成任务通常使用生成模型，如GAN、变分自编码器（VAE）等。
#    - 评估指标：生成任务的评估通常更具挑战性，可以使用多种指标，如生成图像的质量、多样性等。

# 这些是一些常见的任务分类，每种任务类型都有其独特的目标、方法和评估方式。选择适当的任务类型取决于您的具体问题和数据。



# 百度算法搜索关键词热度排名

# GPT (Generative Pre-trained Transformer)：主要用于自然语言处理任务，如文本生成、文本摘要、翻译、问答等。

# CNN (Convolutional Neural Networks)：广泛用于图像识别、图像处理、视频分析和自然语言处理等任务。

# LSTM (Long Short-Term Memory)：一种特殊的循环神经网络，常用于时间序列分析、语音识别、语言模型和自然语言处理等任务。

# BERT (Bidirectional Encoder Representations from Transformers)：用于自然语言处理任务，如语言理解、文本分类、问答系统等。

# XGBoost (eXtreme Gradient Boosting)：是一个高效的机器学习库，主要用于分类、回归和排序任务。

# 决策树 (Decision Trees)：用于分类和回归任务，以树状图的形式对决策过程进行建模。

# SVM (Support Vector Machines)：主要用于分类和回归任务，尤其在小样本数据集上表现良好。

# 逻辑回归 (Logistic Regression)：尽管叫做回归，但主要用于二分类任务。

# KNN (K-Nearest Neighbors)：一种简单的算法，主要用于分类和回归任务。

# scikit-learn函数

# Precision 精确度 from sklearn.metrics import precision_score
# Recall 召回率 from sklearn.metrics import recall_score
# F1 F1指标 from sklearn.metrics import f1_score
# Confusion Matrix 混淆矩阵 from sklearn.metrics import confusion_matrix
# ROC ROC曲线 from sklearn.metrics import roc
# AUC ROC曲线下的面积 from sklearn.metrics import auc