# Загрузим необходимые пакеты
library(ggplot2)
library(RColorBrewer)
library(DAAG)
library(dplyr)


### TASK 1 

#Загрузим данные

mc_menu_data <- read.csv('mc_donalds_data.csv',
                         header = TRUE, sep = ',', encoding = 'UTF-8')

#1.1 Отобрать все данные по категории "Snacks & Sides" (2 балла)
mc_snack_subset <- mc_mendu_data_withoutNA[mc_mendu_data_withoutNA$Category == "Snacks & Sides", ]

#1.2 Отобрать все данные по категориям "Desserts" и "Salads" (2 балла)
mc_sal_dess <- subset(mc_mendu_data_withoutNA, Category == "Desserts" | Category == "Salads")

#1.3 Отобрат все данные кроме категории "Breakfast" (2 балла)
mc_without_breakfast <- subset(mc_mendu_data_withoutNA, Category != "Breakfast")

#1.4 Посчитать число блюд, где калорийность больше чем 500 (2 балла)
sum_more_500 <- sum(mc_mendu_data_withoutNA$Calories>500)

#1.5 Найти самое калорийное блюдо (2 балла)
the_most_caloric <- mc_mendu_data_withoutNA[which.max(mc_mendu_data_withoutNA$Calories),]$Item



### TASK 2 

#Загрузим данные
md <- read.csv('menu.csv')

#Предподготовка 
new_md <- md %>% select(-ends_with("Value."))
mac_data <- cbind(new_md, md %>% select(starts_with("Vit")))
colnames(mac_data) <- c("Category", "Item", "Serving_size", "Calories", "Cal_Fat", "Total_Fat", "Satur_Fat", "Trans_Fat", "Cholesterol", "Sodium","Carbohydrates", "Dietary_fiber","Sugars", "Protein", "Vitamin_A_DV", "Vitamin_C_DV")


#2.1 Найдите число блюд в каждой из категорий, для которых витаминная ценность равна нулю (2 балла)
dplur_task_2.1_breakfast <- nrow(mac_data %>% 
                                   filter(Category == "Breakfast" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_beef_and_pork <- nrow(mac_data %>% 
                                       filter(Category == "Beef & Pork" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_chicken_and_fish <- nrow(mac_data %>% 
                                          filter(Category == "Chicken & Fish" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_salads <- nrow(mac_data %>% 
                                filter(Category == "Salads" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_bsnacks_and_sides <- nrow(mac_data %>% 
                                           filter(Category == "Snacks & Sides" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_desserts <- nrow(mac_data %>% 
                                  filter(Category == "Desserts" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_beverages <- nrow(mac_data %>% 
                                   filter(Category == "Beverages" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_coffee_and_tea <- nrow(mac_data %>% 
                                        filter(Category == "Coffee & Tea" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))
dplur_task_2.1_smoothies_ans_snakes <- nrow(mac_data %>% 
                                              filter(Category == "Smoothies & Shakes" & Vitamin.A....Daily.Value.+Vitamin.C....Daily.Value. == 0))



#2.2 Посчитайте долю калорий, приходящихся на жиры, для блюд из завтраков и округлите значения до 3 знака (2 балла)
dplur_task_2.2 <-  mac_data %>% 
  filter(Category == "Breakfast") %>% 
  mutate(Category, cal_share = round((Cal_Fat / Calories), 3)) %>% 
  select(Category, Item,  Calories, Cal_Fat, cal_share)  
#Будет выведены колонки с Категорией, Названием, Калориями, количеством калорий из жиров и доля

#2.3 Посчитайте среднее значение, медиану и разницу между ними для холестерола (2 балла)
dplur_task_2.3 <- mac_data %>% filter(Category == "Breakfast")%>%select(Category, Item, Cholesterol)
mean_for_cholesterol <- mean(dplur_task_2.3$Cholesterol) #считаем среднее
median_for_cholesterol <- median(dplur_task_2.3$Cholesterol) #считаем медиану
difference = mean_for_cholesterol - median_for_cholesterol #находим разность

#2.4 Для каждой категории найдите блюдо с самым высоким отношением сахаров к углеводам (2 балла)
dplur_task_2.4 <- mac_data %>% group_by(Category) %>% summarise(max(Item, Sugars/Carbohydrates)) 



### TASK 3

# Загрузим данные и немного их отредактируем
data("leafshape")
leafshape$arch <- factor(leafshape$arch, labels = c("Plagiotropic", "Orthotropic"))

#3.1 Распределение (boxplot) длины листа, в зависимости от локации и архитектуры (5 баллов)
ggplot(leafshape, aes(x = location, y = bladelen, fill = arch )) + 
  geom_boxplot() + 
  labs(x = "Location" , y = "Length", title = "Distribution of sheet length, depending on location and architecture", color = "Architecture") + 
  theme() + 
  theme_bw(16) 


#3.2 Сложный график -- violin plot, с разделением по архитекутре листьев (5 баллов)
ggplot(leafshape, aes(fill=arch, x=location, y=bladelen )) + 
  geom_violin(position="dodge", alpha=0.5, outlier.colour="transparent") + 
  facet_grid(~ arch) + 
  labs(title = "Violin Plots for Leafshape data", subtitle = "with separation by leaf architecture", x="Location", y="Length") + 
  theme_bw() + 
  scale_fill_brewer(palette = "Dark2") + 
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
