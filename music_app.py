from typing import List, Tuple, Deque, Optional
from collections import deque
import random
import time
import os

# Try importing pygame for real playback; if unavailable we will simulate.
try:
    import pygame
    PYGAME_AVAILABLE = True
    pygame.mixer.init()
except Exception:
    PYGAME_AVAILABLE = False

# SongInfo tuple: (name, artist, length_seconds)
SongInfo = Tuple[str, str, int]


class Song:
    """Base Song class storing immutable metadata as a tuple."""
    def __init__(self, info: SongInfo):
        self.info: SongInfo = tuple(info)

    def name(self) -> str:
        return self.info[0]

    def artist(self) -> str:
        return self.info[1]

    def length(self) -> int:
        return self.info[2]

    def _fmt_length(self) -> str:
        m, s = divmod(self.length(), 60)
        return f"{m}:{s:02d}"

    def play(self) -> None:
        """Generic play — overridden by subclasses. Default: print simulation."""
        print(f"Playing '{self.name()}' by {self.artist()} [{self._fmt_length()}]")


class LocalSong(Song):
    """Local file: can play a local file path (uses pygame when available)."""
    def __init__(self, info: SongInfo, file_path: str):
        super().__init__(info)
        self.file_path = file_path

    def play(self) -> None:
        print(f"[LOCAL] Requested file: {self.file_path}")
        # If pygame is available and file exists, play it.
        if PYGAME_AVAILABLE and os.path.exists(self.file_path):
            try:
                pygame.mixer.music.load(self.file_path)
                pygame.mixer.music.play()
                print(f"[LOCAL] Playing (real audio): '{self.name()}' — will play up to {self.length()}s")
                # Wait for the song duration (but not longer than a safety cap)
                # Safety: cap wait to 30s for demo, or actual length if smaller.
                wait_time = min(self.length(), 30)
                time.sleep(wait_time)
                pygame.mixer.music.stop()
                print(f"[LOCAL] Stopped '{self.name()}'\n")
            except Exception as e:
                print("[LOCAL] Playback failed (pygame). Falling back to simulation.")
                print(f"[LOCAL] Error: {e}")
                super().play()
                time.sleep(0.2)
                print(f"[LOCAL] Finished (simulated) '{self.name()}'\n")
        else:
            if not PYGAME_AVAILABLE:
                print("[LOCAL] pygame not available — simulating playback.")
            else:
                print("[LOCAL] File not found — simulating playback.")
            super().play()
            time.sleep(0.2)
            print(f"[LOCAL] Finished (simulated) '{self.name()}'\n")

    def __repr__(self):
        return f"LocalSong({self.info}, '{self.file_path}')"


class OnlineSong(Song):
    """OnlineSong simulates streaming from a URL/provider."""
    def __init__(self, info: SongInfo, stream_url: str, provider: str = "Unknown"):
        super().__init__(info)
        self.stream_url = stream_url
        self.provider = provider

    def play(self) -> None:
        print(f"[STREAM] Connecting to {self.provider} at {self.stream_url} ...")
        super().play()
        # Simulate buffering + streaming for a short time
        time.sleep(0.3)
        print(f"[STREAM] Finished streaming '{self.name()}'\n")

    def __repr__(self):
        return f"OnlineSong({self.info}, '{self.stream_url}', provider='{self.provider}')"


class Playlist:
    """Playlist stores Song objects and manages recently played, shuffle, search, etc."""
    def __init__(self, name: str = "My Playlist", recently_played_capacity: int = 5):
        self.name = name
        self.songs: List[Song] = []
        self.recently_played: Deque[Song] = deque(maxlen=recently_played_capacity)

    # Add / remove
    def add_song(self, song: Song) -> None:
        self.songs.append(song)
        print(f"Added: {song.name()} by {song.artist()}")

    def remove_song_by_index(self, index: int) -> Optional[Song]:
        if 0 <= index < len(self.songs):
            removed = self.songs.pop(index)
            print(f"Removed: {removed.name()} by {removed.artist()}")
            return removed
        print("Invalid index. No song removed.")
        return None

    def remove_song_by_name(self, name: str) -> Optional[Song]:
        for i, s in enumerate(self.songs):
            if s.name().lower() == name.lower():
                return self.remove_song_by_index(i)
        print(f"No song named '{name}' found.")
        return None

    # Display
    def show(self) -> None:
        if not self.songs:
            print(f"Playlist '{self.name}' is empty.")
            return
        print(f"Playlist: {self.name} — {len(self.songs)} songs")
        for i, s in enumerate(self.songs, start=1):
            print(f"{i:2d}. {s.name()} - {s.artist()} [{s._fmt_length()}]")

    # Play
    def play_song(self, index: int) -> None:
        """User-facing index is 1-based."""
        i = index - 1
        if 0 <= i < len(self.songs):
            song = self.songs[i]
            song.play()           # polymorphic: works for LocalSong or OnlineSong
            self._add_to_recent(song)
        else:
            print("Invalid song number.")

    def play_next(self) -> None:
        if not self.songs:
            print("Playlist empty.")
            return
        # Simple behavior: play first in list
        self.play_song(1)

    def _add_to_recent(self, song: Song) -> None:
        # Keep uniqueness in recently_played and append as most recent
        try:
            self.recently_played.remove(song)
        except ValueError:
            pass
        self.recently_played.append(song)

    def show_recent(self) -> None:
        if not self.recently_played:
            print("No recently played songs.")
            return
        print("Recently played (oldest -> newest):")
        for s in self.recently_played:
            print(f"- {s.name()} by {s.artist()} [{s._fmt_length()}]")

    # Shuffle / search / clear
    def shuffle(self) -> None:
        random.shuffle(self.songs)
        print("Playlist shuffled.")

    def find(self, query: str) -> List[int]:
        q = query.lower()
        return [i + 1 for i, s in enumerate(self.songs) if q in s.name().lower() or q in s.artist().lower()]

    def clear(self) -> None:
        self.songs.clear()
        self.recently_played.clear()
        print("Playlist and recently played cleared.")


# ---------------- Demo usage ----------------
def demo():
    # Use raw strings for Windows paths; update these to real files on your computer if you want playback.
    s1_info: SongInfo = ("Jo Bheji Thi Dua", "Arijit Singh", 215)
    s2_info: SongInfo = ("Thodi Jagah", "Arijit Singh", 189)
    s3_info: SongInfo = ("Tum Hi Aana", "Jubin Nautiyal", 240)

    s1 = LocalSong(s1_info, file_path=r"D:\\Playlists\\Jo_Bheji_Thi.mp3")
    s2 = OnlineSong(s2_info, stream_url="http://bit.ly/Thodi-Jagah", provider="ExampleStream")
    s3 = LocalSong(s3_info, file_path=r"D:\\Playlists\\Tum_Hi_Aana.mp3")

    pl = Playlist(name="My Hindi Playlist", recently_played_capacity=4)
    pl.add_song(s1)
    pl.add_song(s2)
    pl.add_song(s3)

    print()
    pl.show()
    print()

    # Play first and second songs
    pl.play_song(1)
    pl.play_song(2)

    # Recently played
    pl.show_recent()
    print()

    # Shuffle and display
    pl.shuffle()
    pl.show()
    print()

    # Find
    matches = pl.find("Jo Bheji")
    print("Search results for 'Jo Bheji':", matches)
    print()

    # Remove by name (example - remove Tum Hi Aana)
    pl.remove_song_by_name("Tum Hi Aana")
    pl.show()
    print()

    # Clear playlist
    pl.clear()
    pl.show()


if __name__ == "__main__":
    demo()
