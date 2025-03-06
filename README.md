## A repo for focusing on CELERY

1. initiate a project
2. setup Celery 
3. start the workers


# Installing Redis (Without Docker)

This guide provides step-by-step instructions for installing a basic version of Redis on macOS, Windows, Arch Linux, and Ubuntu.

---

## macOS

### Using Homebrew

1. **Install Homebrew** (if you don’t have it):  
   Open your Terminal and run:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Redis:**
   ```bash
   brew install redis
   ```

3. **Start Redis:**
   - To run Redis as a background service:
     ```bash
     brew services start redis
     ```
   - Alternatively, run Redis manually:
     ```bash
     redis-server /usr/local/etc/redis.conf
     ```

4. **Test your installation:**
   ```bash
   redis-cli ping
   ```
   You should see:
   ```
   PONG
   ```

---

## Windows

Redis isn’t officially supported on Windows, but you have two options:

### Option 1: Using Windows Subsystem for Linux (WSL)

1. **Install WSL** and choose an Ubuntu distribution.
2. **Follow the Ubuntu instructions** below after launching your WSL/Ubuntu terminal.

### Option 2: Using a Community Port via Chocolatey

1. **Install Chocolatey** (if you don’t have it):  
   Open an elevated (Administrator) PowerShell and run:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; \`
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \`
   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

2. **Install Redis using Chocolatey:**
   ```powershell
   choco install redis-64
   ```

3. **Run Redis:**  
   Locate `redis-server.exe` (typically found in `C:\ProgramData\chocolatey\lib\redis-64\tools`) and run it from a command prompt.

*Note:* The Windows port is maintained by the community and might differ slightly from the Unix version. For a more stable production-like environment, using WSL is often recommended.

---

## Arch Linux

1. **Install Redis from the Arch repositories:**
   ```bash
   sudo pacman -S redis
   ```

2. **Configure Redis (optional):**  
   Edit the configuration file located at `/etc/redis/redis.conf` if needed.

3. **Enable and start the Redis service:**
   ```bash
   sudo systemctl enable redis.service
   sudo systemctl start redis.service
   ```

4. **Test your installation:**
   ```bash
   redis-cli ping
   ```
   You should receive:
   ```
   PONG
   ```

---

## Ubuntu

1. **Update your package index:**
   ```bash
   sudo apt update
   ```

2. **Install Redis:**
   ```bash
   sudo apt install redis-server
   ```

3. **Configure Redis (optional):**  
   The main configuration file is located at \`/etc/redis/redis.conf\`.

4. **Enable and start Redis:**
   ```bash
   sudo systemctl enable redis-server
   sudo systemctl start redis-server
   ```

5. **Test your installation:**
   ```bash
   redis-cli ping
   ```
   You should see:
   ```
   PONG
   ```

---



