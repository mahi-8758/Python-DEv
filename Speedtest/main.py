import speedtest
import time
from datetime import datetime
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_pdf import PdfPages
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import subprocess
import platform

# Suppress locale warnings
os.environ['LANG'] = 'C.UTF-8'
os.environ['LC_ALL'] = 'C.UTF-8'

# Data storage
timestamps = []
download_speeds = []
upload_speeds = []
pings = []

class SpeedTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test Monitor")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#27394c")
        
        self.is_testing = False
        self.test_thread = None
        self.last_pdf_path = None
        
        # Header
        header = tk.Frame(root, bg='#34495e', pady=15)
        header.pack(fill='x')
        
        title = tk.Label(header, text="Internet Speed Test Monitor", 
                        font=('Times New Roman', 20, 'bold'), bg='#34495e', fg='white')
        title.pack()
        
        # Control Frame - Row 1
        control_frame1 = tk.Frame(root, bg='#2c3e50', pady=5)
        control_frame1.pack(fill='x')
        
        self.start_btn = tk.Button(control_frame1, text="Start", 
                                   command=self.start_testing, 
                                   bg="#1dc362", fg='white', 
                                   font=('Arial', 12, 'bold'),
                                   width=15, height=2)
        self.start_btn.pack(side='left', padx=10)
        
        self.stop_btn = tk.Button(control_frame1, text="Stop", 
                                  command=self.stop_testing, 
                                  bg='#e74c3c', fg='white', 
                                  font=('Arial', 12, 'bold'),
                                  width=15, height=2, state='disabled')
        self.stop_btn.pack(side='right', padx=10)
        
        self.reset_btn = tk.Button(control_frame1, text="Reset", 
                                   command=self.reset_testing, 
                                   bg='#e67e22', fg='white', 
                                   font=('Arial', 12, 'bold'),
                                   width=15, height=2)
        self.reset_btn.pack(side='right', padx=10)

        self.export_btn = tk.Button(control_frame1, text="Export", 
                                    command=self.export_pdf, 
                                    bg='#3498db', fg='white', 
                                    font=('Arial', 12, 'bold'),
                                    width=15, height=2, state='disabled')
        self.export_btn.pack(side='left', padx=10)
        
        self.show_pdf_btn = tk.Button(control_frame1, text="Show", 
                                      command=self.show_pdf, 
                                      bg='#9b59b6', fg='white', 
                                      font=('Arial', 12, 'bold'),
                                      width=15, height=2, state='disabled')
        self.show_pdf_btn.pack(side='left', padx=10)
        
        stats_frame = tk.LabelFrame(root, text="Current Statistics", 
                                   bg='#34495e', fg='white', 
                                   font=('Arial', 12, 'bold'), 
                                   pady=10, padx=10)
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        # Create stats display
        stats_inner = tk.Frame(stats_frame, bg='#34495e')
        stats_inner.pack()
        
        # Download
        tk.Label(stats_inner, text="Download:", bg='#34495e', fg='#3498db', 
                font=('Arial', 11, 'bold')).grid(row=0, column=0, padx=10, sticky='w')
        self.download_label = tk.Label(stats_inner, text="-- Mbps", 
                                       bg='#34495e', fg='white', 
                                       font=('Arial', 14, 'bold'))
        self.download_label.grid(row=0, column=1, padx=10)
        
        # Upload
        tk.Label(stats_inner, text="Upload:", bg='#34495e', fg='#e74c3c', 
                font=('Arial', 11, 'bold')).grid(row=0, column=2, padx=10, sticky='w')
        self.upload_label = tk.Label(stats_inner, text="-- Mbps", 
                                     bg='#34495e', fg='white', 
                                     font=('Arial', 14, 'bold'))
        self.upload_label.grid(row=0, column=3, padx=10)
        
        # Ping
        tk.Label(stats_inner, text="Ping:", bg='#34495e', fg='#2ecc71', 
                font=('Arial', 11, 'bold')).grid(row=0, column=4, padx=10, sticky='w')
        self.ping_label = tk.Label(stats_inner, text="-- ms", 
                                   bg='#34495e', fg='white', 
                                   font=('Arial', 14, 'bold'))
        self.ping_label.grid(row=0, column=5, padx=10)
        
        # Tests counter
        self.test_count_label = tk.Label(stats_inner, text="Tests: 0", 
                                        bg='#34495e', fg='#f39c12', 
                                        font=('Arial', 11, 'bold'))
        self.test_count_label.grid(row=1, column=0, columnspan=6, pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(root, mode='indeterminate')
        self.progress.pack(fill='x', padx=20, pady=5)
        
        # Log Frame
        log_frame = tk.LabelFrame(root, text="Test Log", 
                                 bg='#34495e', fg='white', 
                                 font=('Arial', 12, 'bold'))
        log_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, 
                                                  height=15, 
                                                  bg='#1c2833', 
                                                  fg='#ecf0f1', 
                                                  font=('Courier', 10))
        self.log_text.pack(fill='both', expand=True, padx=5, pady=5)
        
    def log(self, message):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        
    def start_testing(self):
        global timestamps, download_speeds, upload_speeds, pings
        timestamps = []
        download_speeds = []
        upload_speeds = []
        pings = []
        
        self.is_testing = True
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.reset_btn.config(state='disabled')
        self.export_btn.config(state='disabled')
        self.show_pdf_btn.config(state='disabled')
        self.progress.start(10)
        
        self.log("Starting real-time internet speed monitor...")
        self.log("="*60)
        
        self.test_thread = threading.Thread(target=self.run_speed_test, daemon=True)
        self.test_thread.start()
        
    def stop_testing(self):
        self.is_testing = False
        self.stop_btn.config(state='disabled')
        self.reset_btn.config(state='normal')
        self.progress.stop()
        
        if len(timestamps) > 0:
            self.export_btn.config(state='normal')
            self.log("="*60)
            self.log(f"Testing stopped. Total tests completed: {len(timestamps)}")
        else:
            self.start_btn.config(state='normal')
            self.log("No data collected.")
    
    def reset_testing(self):
        """Reset all data and UI to initial state"""
        global timestamps, download_speeds, upload_speeds, pings
        
        # Confirm reset if data exists
        if len(timestamps) > 0:
            result = messagebox.askyesno("Confirm Reset", 
                                        "Are you sure you want to reset all data?\nThis will clear all test results.")
            if not result:
                return
        
        # Stop testing if running
        if self.is_testing:
            self.is_testing = False
            self.progress.stop()
        
        # Clear all data
        timestamps = []
        download_speeds = []
        upload_speeds = []
        pings = []
        self.last_pdf_path = None
        
        # Reset UI elements
        self.download_label.config(text="-- Mbps")
        self.upload_label.config(text="-- Mbps")
        self.ping_label.config(text="-- ms")
        self.test_count_label.config(text="Tests: 0")
        
        # Reset button states
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.reset_btn.config(state='normal')
        self.export_btn.config(state='disabled')
        self.show_pdf_btn.config(state='disabled')
        
        # Clear log
        self.log_text.delete(1.0, tk.END)
        
        self.log("✓ All data has been reset!")
        self.log("Ready to start new testing session.")
        self.log("="*60)
        
    def run_speed_test(self):
        test_count = 1
        consecutive_errors = 0
        max_consecutive_errors = 3
        
        while self.is_testing:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.log(f"\n--- Test #{test_count} at {timestamp} ---")
            
            try:
                # Create new Speedtest instance with secure mode
                st = speedtest.Speedtest(secure=True)
                
                self.log("Finding best server...")
                st.get_best_server()
                
                self.log("Testing download speed...")
                download_speed = st.download(threads=None)
                
                self.log("Testing upload speed...")
                upload_speed = st.upload(threads=None)
                
                ping = st.results.ping
                
                download_mbps = download_speed / (1024 * 1024)
                upload_mbps = upload_speed / (1024 * 1024)
                
                # Store data
                timestamps.append(datetime.now())
                download_speeds.append(download_mbps)
                upload_speeds.append(upload_mbps)
                pings.append(ping)
                
                # Update GUI
                self.root.after(0, self.update_stats, download_mbps, upload_mbps, ping, test_count)
                
                self.log(f"✓ Ping: {ping:.2f} ms")
                self.log(f"✓ Download: {download_mbps:.2f} Mbps")
                self.log(f"✓ Upload: {upload_mbps:.2f} Mbps")
                self.log("-"*60)
                
                # Reset error counter on success
                consecutive_errors = 0
                test_count += 1
                
                # Wait 30 seconds between successful tests to avoid rate limiting
                time.sleep(30)
                
            except speedtest.ConfigRetrievalError as e:
                consecutive_errors += 1
                self.log(f"✗ Configuration Error: {str(e)}")
                self.log(f"Retrying in 20 seconds... (Error {consecutive_errors}/{max_consecutive_errors})")
                self.log("-"*60)
                
                if consecutive_errors >= max_consecutive_errors:
                    self.log(f"\n⚠ Too many consecutive errors. Stopping tests.")
                    self.root.after(0, self.stop_testing)
                    break
                
                time.sleep(10)
                
            except Exception as e:
                consecutive_errors += 1
                self.log(f"✗ Error: {str(e)}")
                self.log(f"Retrying in 20 seconds... (Error {consecutive_errors}/{max_consecutive_errors})")
                self.log("-"*60)
                
                if consecutive_errors >= max_consecutive_errors:
                    self.log(f"\n⚠ Too many consecutive errors. Stopping tests.")
                    self.root.after(0, self.stop_testing)
                    break
                
                time.sleep(10)
        
        self.root.after(0, self.start_btn.config, {'state': 'normal'})
        
    def update_stats(self, download, upload, ping, count):
        self.download_label.config(text=f"{download:.2f} Mbps")
        self.upload_label.config(text=f"{upload:.2f} Mbps")
        self.ping_label.config(text=f"{ping:.2f} ms")
        self.test_count_label.config(text=f"Tests: {count}")
        
    def export_pdf(self):
        if len(timestamps) == 0:
            self.log("No data to export!")
            return
        
        self.log("\nGenerating PDF report...")
        
        # Create Results folder
        results_folder = os.path.join(os.path.dirname(__file__), 'Results')
        os.makedirs(results_folder, exist_ok=True)
        
        # Calculate statistics
        avg_download = sum(download_speeds) / len(download_speeds)
        avg_upload = sum(upload_speeds) / len(upload_speeds)
        avg_ping = sum(pings) / len(pings)
        
        max_download = max(download_speeds)
        max_upload = max(upload_speeds)
        min_ping = min(pings)
        max_ping = max(pings)
        
        # Create figure
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Internet Speed Test Results', fontsize=16, weight='bold')
        
        # Plot 1: Download and Upload Speed
        ax1.plot(timestamps, download_speeds, 'b-', label='Download', linewidth=2, marker='o')
        ax1.plot(timestamps, upload_speeds, 'r-', label='Upload', linewidth=2, marker='o')
        ax1.axhline(y=avg_download, color='b', linestyle='--', alpha=0.5)
        ax1.axhline(y=avg_upload, color='r', linestyle='--', alpha=0.5)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Speed (Mbps)')
        ax1.set_title('Download & Upload Speed Over Time')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        # Plot 2: Ping
        ax2.plot(timestamps, pings, 'g-', linewidth=2, marker='o')
        ax2.axhline(y=avg_ping, color='orange', linestyle='--', alpha=0.5)
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Ping (ms)')
        ax2.set_title('Latency Over Time')
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis='x', rotation=45)
        
        # Plot 3: Statistics
        ax3.axis('off')
        stats_text = f"""
    STATISTICS
    {'='*30}
    Total Tests: {len(timestamps)}
    
    DOWNLOAD SPEED
    Average: {avg_download:.2f} Mbps
    Maximum: {max_download:.2f} Mbps
    Minimum: {min(download_speeds):.2f} Mbps
    
    UPLOAD SPEED
    Average: {avg_upload:.2f} Mbps
    Maximum: {max_upload:.2f} Mbps
    Minimum: {min(upload_speeds):.2f} Mbps
    
    PING
    Average: {avg_ping:.2f} ms
    Minimum: {min_ping:.2f} ms
    Maximum: {max_ping:.2f} ms
        """
        ax3.text(0.1, 0.9, stats_text, transform=ax3.transAxes, 
                fontsize=11, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Plot 4: Bar chart
        categories = ['Download\n(Avg)', 'Upload\n(Avg)', 'Ping\n(Avg)']
        values = [avg_download, avg_upload, avg_ping]
        colors = ['blue', 'red', 'green']
        
        bars = ax4.bar(categories, values, color=colors, alpha=0.7)
        ax4.set_ylabel('Value')
        ax4.set_title('Average Values Comparison')
        ax4.grid(True, alpha=0.3, axis='y')
        
        for bar in bars:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        
        # Save PDF
        timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        pdf_filename = f'speedtest_results_{timestamp_str}.pdf'
        pdf_filepath = os.path.join(results_folder, pdf_filename)
        
        with PdfPages(pdf_filepath) as pdf:
            pdf.savefig(fig, bbox_inches='tight')
            
            d = pdf.infodict()
            d['Title'] = 'Internet Speed Test Results'
            d['Author'] = 'Speed Test Monitor'
            d['Subject'] = f'Speed test conducted on {datetime.now().strftime("%Y-%m-%d")}'
            d['Keywords'] = 'Internet Speed, Download, Upload, Ping, Network'
            d['CreationDate'] = datetime.now()
        
        plt.close(fig)
        
        # Store the PDF path and enable Show PDF button
        self.last_pdf_path = pdf_filepath
        self.show_pdf_btn.config(state='normal')
        
        self.log(f"✓ PDF saved to: {pdf_filepath}")
        self.log("Export completed successfully!")
        
    def show_pdf(self):
        if not self.last_pdf_path or not os.path.exists(self.last_pdf_path):
            messagebox.showerror("Error", "No PDF file found. Please export PDF first.")
            return
        
        self.log(f"\nOpening PDF: {self.last_pdf_path}")
        
        try:
            system = platform.system()
            
            if system == 'Linux':
                # Suppress stderr to avoid locale warnings
                subprocess.run(['xdg-open', self.last_pdf_path], 
                             stderr=subprocess.DEVNULL)
            elif system == 'Windows':
                os.startfile(self.last_pdf_path)
            elif system == 'Darwin':  # macOS
                subprocess.run(['open', self.last_pdf_path])
            else:
                messagebox.showwarning("Warning", f"Unable to open PDF on {system}")
                return
            
            self.log("✓ PDF opened successfully!")
            
        except Exception as e:
            self.log(f"✗ Error opening PDF: {e}")
            messagebox.showerror("Error", f"Failed to open PDF:\n{str(e)}")

# Create and run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestGUI(root)
    root.mainloop()