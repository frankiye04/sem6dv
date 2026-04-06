library(ggplot2)
# --- 1. Create Sample Data ---
data <- data.frame(Value = c(23, 45, 56, 67, 34, 45, 23, 45, 56, 67, 78, 89, 45, 56, 67))
# --- 2. Set save location ---
save_path <- "D:/DV/" # Make sure this folder exists
# Create folder if it doesn't exist
if (!dir.exists(save_path)) {
 dir.create(save_path, recursive = TRUE)
}
# --- 3. Histogram ---
hist_plot <- ggplot(data, aes(x = Value)) +
 geom_histogram(binwidth = 10, fill = "skyblue", color = "black") +
 ggtitle("Histogram of Values") +
 xlab("Values") +
 ylab("Frequency")
# Display histogram
print(hist_plot)
# Save histogram as JPG using jpeg() device
jpeg(filename = paste0(save_path, "histogram.jpg"), width = 800, height = 600, res = 150)
print(hist_plot)
dev.off() # Close the device
# Wait for user input
cat("Press [Enter] after viewing the histogram to continue...\n")
readline() # Pause until Enter is pressed
# Optional 10-second delay
cat("Waiting 10 seconds before showing density plot...\n")
Sys.sleep(10)
# --- 4. Density Plot ---
density_plot <- ggplot(data, aes(x = Value)) +
 geom_density(fill = "lightgreen", alpha = 0.5) +
 ggtitle("Density Plot of Values") +
 xlab("Values") +
 ylab("Density")
# Display density plot
print(density_plot)
# Save density plot as JPG
jpeg(filename = paste0(save_path, "density_plot.jpg"), width = 800, height = 600, res = 150)
print(density_plot)
dev.off() # Close the device
cat("Both plots saved as JPG in D:/DV/ folder.\n")
##Run the Script Using source()
#In the R console, type:
#source("D:/DV/a.R")
