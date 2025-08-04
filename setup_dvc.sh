#!/bin/bash

echo "📦 Checking and installing DVC and rclone..."

# Check and install DVC
if ! command -v dvc &> /dev/null; then
  echo "🚧 DVC not found. Installing DVC..."
  python -m pip install --user dvc[gdrive] || { echo "❌ Failed to install DVC"; exit 1; }
else
  echo "✅ DVC is already installed."
fi

# Check and install rclone
if ! command -v rclone &> /dev/null; then
  echo "🚧 rclone not found. Installing rclone..."
  python -m pip install --user rclone || { echo "❌ Failed to install rclone"; exit 1; }
else
  echo "✅ rclone is already installed."
fi

echo "✅ Initializing DVC in this project..."
dvc init

echo "🎯 Tracking model files with DVC..."
dvc add models/attack_type_model.pkl
dvc add models/defense_model.pkl
dvc add models/loss_model.pkl
dvc add models/resolution_model.pkl
dvc add models/vulnerability_model.pkl

echo "📁 Adding DVC files to Git..."
git add .dvc .gitignore
git add models/*.dvc
git commit -m "Initialize DVC and track model files"

echo "📌 Configuring remote storage (Google Drive via rclone)..."

# Change these if needed
DVC_REMOTE_NAME="gdrive_remote"
RCLONE_REMOTE_NAME="mygdrive"  # Defined in your rclone config
GDRIVE_FOLDER_ID="1qjxnCAOuVYLigDTA0nK_IeNoGTPQSLCQ"

dvc remote add -d $DVC_REMOTE_NAME gdrive://$GDRIVE_FOLDER_ID
dvc remote modify $DVC_REMOTE_NAME rclone_config $RCLONE_REMOTE_NAME

echo "☁️ Pushing model to Google Drive..."
dvc push

echo "✅ Model pushed to remote storage. Now push your Git repo..."
