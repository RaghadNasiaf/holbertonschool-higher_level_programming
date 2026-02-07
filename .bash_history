git config --global user.email "naseefraghad@gmail.com"
git config --global user.name "RaghadNasiaf"
mkdir -p ~/holbertonschool-higher_level_programming/python-server_side_rendering
cd ~/holbertonschool-higher_level_programming/python-server_side_rendering
cat > template.txt << 'EOF'
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
EOF

git add task_00_intro.py
git commit -m "Task 0: Implement basic templating program"
git push origin main
git config --global user.email "naseefraghad@gmail.com"
git config --global user.name "RaghadNasiaf"
cd ~
git init
git remote add origin https://github.com/RaghadNasiaf/holbertonschool-higher_level_programming.git
git pull origin main --rebase
mkdir -p python-server_side_rendering
cd python-server_side_rendering
cd ~/
