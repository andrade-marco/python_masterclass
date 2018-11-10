# Music browser
import sqlite3
import tkinter

# Scrollbox class
class Scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = 'SELECT ' + self.field + ', _id' + ' FROM ' + self.table
        if sort_order:
            self.sql_sort = ' ORDER BY ' + ','.join(sort_order)
        else:
            self.sql_sort = ' ORDER BY ' + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value
        if link_value and self.link_field:
            sql = self.sql_select + ' WHERE ' + self.link_field + '=?' + self.sql_sort
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            if self.curselection():
                index = self.curselection()[0]
                value = (self.get(index),)

                if self.link_value:
                    value = (value[0], self.link_value)
                    sql_where = ' WHERE ' + self.field + '=? AND ' + self.link_field + '=?'
                else:
                    sql_where = ' WHERE ' + self.field + '=?'
                link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
                self.linked_box.requery(link_id)


if __name__ == '__main__':
    # DB connection
    db = sqlite3.connect('music.db')

    # GUI
    mainWindow = tkinter.Tk()
    mainWindow.title('Music Browser')
    mainWindow.geometry('1024x768')

    # Configuring columns and rows
    # Three regular columns and a spacer column
    # Two smaller rows and two content rows
    for i in range(0, 4):
        col_weight = 2 if i < 3 else 1
        row_weight = 5 if 0 < i < 3 else 1
        mainWindow.columnconfigure(i, weight=col_weight)
        mainWindow.rowconfigure(i, weight=row_weight)

    # Labels
    label_content = [('Artists', 0), ('Albums', 1), ('Songs', 2)]
    for label, col in label_content:
        tkinter.Label(mainWindow, text=label).grid(row=0, column=col)

    # Configuring listboxes
    # List variables
    album_lv = tkinter.Variable(mainWindow)
    album_lv.set(('Choose an artist',))

    song_lv = tkinter.Variable(mainWindow)
    song_lv.set(('Choose an album',))

    # Listboxes and scrollbars
    artists_list = DataListBox(mainWindow, db, 'artists', 'name')
    album_list = DataListBox(mainWindow, db, 'albums', 'name', sort_order=('name',))
    song_list = DataListBox(mainWindow, db, 'songs', 'title', sort_order=('track','title'))

    for index, list in enumerate([artists_list, album_list, song_list]):
        span = 2 if index == 0 else 1
        list.grid(row=1, column=index, sticky='nsew', rowspan=span, padx=(30,0))
        list.config(border=2, relief='sunken')

    # Populating artists box
    artists_list.link(album_list, 'artist')
    album_list.link(song_list, 'album')
    artists_list.requery()

    # Main loop
    mainWindow.mainloop()
    db.close()
